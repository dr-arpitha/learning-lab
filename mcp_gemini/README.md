Beginner’s Guide to Model Context Protocol
=

If you’ve been following the progress of AI tools especially developer tools or assistants that connect with external data, you may have heard about the Model Context Protocol, or MCP. It’s a new open-source standard designed to make AI models (like ChatGPT, Gemini) far more capable by letting them safely interact with tools, data sources, and applications.

This guide explains MCP in simple terms and walks through our Python code that lets Gemini convert natural language into real command-line operations, safely executed via an MCP server.
____
What is MCP?
------------

The **Model Context Protocol (MCP)** is an open standard that allows AI models to connect to tools, databases, APIs, or even your local files _in a consistent, safe, and structured way_.

Think of it like a universal plug for AI systems:

*   Apps can expose features and data through MCP
    
*   Models can use those features safely
    
*   Both sides follow the same set of rules
    

Before MCP, every model and every tool needed its own custom integration. Everything was proprietary. MCP makes this open, standardized, and modular.

An MCP system has two main parts:

**MCP Client:**

This is the AI assistant (like ChatGPT, Claude, Cursor) that wants to call external tools.

**MCP Server:**

A tool, API, or service that exposes capabilities through MCP.

Examples:

*   An MCP server that reads/writes local files
    
*   An MCP server that queries a database
    
*   An MCP server that accesses Google Calendar
    
*   An MCP server that performs code analysis
    
*   A custom tool you write
    

The model communicates with the server using a structured JSON-RPC style protocol.
____
### Why MCP Exists ?

#### Without MCP:

*   Tools must build custom integrations for each AI model
    
*   Developers must learn multiple proprietary systems
    
*   Local tools (like your filesystem) have no safe standardized interface
    
*   Sharing tools across models is hard or impossible
    

#### With MCP:

*   A tool only needs to implement one protocol
    
*   It becomes compatible with _any_ model that supports MCP
    
*   Models can safely interact with:
    
    *   APIs
        
    *   Databases
        
    *   Local files
        
    *   Developer tools
        
    *   Workflows
        
    *   Knowledge bases
        
*   You get portability, consistency, and safety
    

In short: MCP is like USB for AI — a universal connection standard.
____
### Our Python Script Explained Step-by-Step

#### **→ Prerequisites**

Install all the prerequisites:

```
pip install google-generativeai mcp
```

#### → Define how to launch the MCP Server

Our MCP server is a Python script that exposes command-line operations as tools:

```
script_path=”/Users/.../commandline_server.py” 
```
We use StdioServerParameters to run it:

```
server_params = StdioServerParameters(
    command="python",
    args=[script_path]
)
```

This means:

*   Our Python “client” will launch the MCP server
    
*   Communication happens over standard input/output (stdio)
    

#### → Connect to the MCP server

```
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session: 
        await session.initialize()
```

This opens a communication channel to the server. 
The client asks the server:

> “Hello, what tools do you provide?”

#### → Let the model discover tools dynamically

```
mcp_tools = await session.list_tools()  
```

Our command-line MCP server might expose various tools that are turned into Gemini tool declarations:

```
tools = [types.Tool( function_declarations=[ ... ])
    for tool in mcp_tools.tools]   
```

This is how the model learns:

*   what it _can_ do
    
*   what arguments each tool expects
    
*   how to call them safely
    

#### → We Ask Gemini to interpret the natural-language command

Our prompt:

```
prompt = “Append to file : ‘mcp_test_file.txt’ and write a note about MCP”   
```

Gemini receives the prompt and the list of available tools

So it can reason like:

> “This sounds like an append-to-file command. Use the defined tool with arguments: filename = mcp\_test\_file.txt, content = ”

#### → Check if the model wants to call a tool

```
if response.candidates[0].content.parts[0].function_call:
```

If yes, you extract the function call:

```
function_call = ...  print(f”{function_call.name} will be executed with arguments: {function_call.args}”)
```

#### → Execute the tool on the MCP server

```
result = await session.call_tool(function_call.name,arguments=dict(function_call.args))   
```

This is where real command-line actions happen:

- file creation 
- appending
- deleting
- reading
- any custom actions the server exposes

The MCP server runs these safely and returns structured output.

#### → Display results

```
print(result.content[0].text)
```

If the tool returns JSON or text, it prints it.
____
Final Thoughts
==============

The Model Context Protocol is one of the most significant developments in AI tooling:It turns models from passive text generators into active agents that can work with real data, real tools, and real workflows, _all in a safe and standardized way_.

#### **References**

*   [MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
    
*   [Builder.io Guide](https://www.builder.io/blog/model-context-protocol)
    
*   [Build MCP Server](https://modelcontextprotocol.io/docs/develop/build-server)
    
*   [MCP Flight Search](https://medium.com/google-cloud/model-context-protocol-mcp-with-google-gemini-llm-a-deep-dive-full-code-ea16e3fac9a3)
    
*   [MCP Command Line](https://medium.com/@chandravanshi.pankaj.ai/9031f000a35d)