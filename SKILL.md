# agent Skill

Use this skill to work with Norm module `agent` version 7. Use only declarations listed below.

## `agent`

Source: `agent.norm`

### `AgentSession`

Public API declaration AgentSession.

```norm
class AgentSession
```

#### `id`

Returns the generated identifier shared by all persistence providers.

```norm
String id()
```

Returns: `String`

#### `AgentSession`

Creates an Agent session.

```norm
AgentSession(SessionStore store)
```

Parameters:

- `store`: `SessionStore`
The session store.


#### `append`

Public API declaration append.

```norm
Void append(JsonValue item)
```

Parameters:

- `item`: `JsonValue`
The JSON item.


Returns: `Void`

#### `items`

Public API declaration items.

```norm
List<JsonValue> items()
```

Returns: `List<JsonValue>`

#### `addContext`

Public API declaration addContext.

```norm
Void addContext(String text)
```

Parameters:

- `text`: `String`
The context text.


Returns: `Void`

### `ToolScope`

Public API declaration ToolScope.

```norm
interface ToolScope
```

#### `complete`

Completes the tool scope and returns optional feedback.

```norm
String? complete()
```

Returns: `String?`

#### `close`

Closes the tool scope.

```norm
Void close()
```

Returns: `Void`

### `Agent`

Public API declaration Agent.

```norm
class Agent
```

#### `Agent`

Creates an Agent with tools, Skills, and model configuration.

```norm
Agent(String apiKey, String model, String endpoint, String? instruction, List<Skill> skills, List<Function<?>> tools, Integer maximumRounds, Integer maximumOutputTokens, Function<List<Function<?>>()>? toolProvider, Function<ToolScope()>? beginToolScope, Function<String?()>? contextProvider, List<McpToolProvider> mcp, HeaderMap headers, List<PersistProvider> persist)
```

Parameters:

- `apiKey`: `String`
The API key.

- `model`: `String`
The model name.

- `endpoint`: `String`
The endpoint URL.

- `instruction`: `String?`
The instructions.

- `skills`: `List<Skill>`
The initial Skills.

- `tools`: `List<Function<?>>`
The initial tools.

- `maximumRounds`: `Integer`
The maximum rounds.

- `maximumOutputTokens`: `Integer`
The maximum output tokens.

- `toolProvider`: `Function<List<Function<?>>()>?`
The dynamic tool provider.

- `beginToolScope`: `Function<ToolScope()>?`
The tool scope factory.

- `contextProvider`: `Function<String?()>?`
The context provider.

- `mcp`: `List<McpToolProvider>`
The MCP providers.

- `headers`: `HeaderMap`
Additional model HTTP headers forwarded to the protocol client.

- `persist`: `List<PersistProvider>`
Conversation log providers, empty by default.


#### `Agent`

Creates an Agent with tools, Skills, and model configuration.

```norm
Agent(String apiKey, String model, String endpoint, Array<String> headers, String? instruction, List<Skill> skills, List<Function<?>> tools, Integer maximumRounds, Integer maximumOutputTokens, Function<List<Function<?>>()>? toolProvider, Function<ToolScope()>? beginToolScope, Function<String?()>? contextProvider, List<McpToolProvider> mcp, List<PersistProvider> persist)
```

Parameters:

- `apiKey`: `String`
The API key.

- `model`: `String`
The model name.

- `endpoint`: `String`
The endpoint URL.

- `headers`: `Array<String>`
Additional model HTTP headers forwarded to the protocol client.

- `instruction`: `String?`
The instructions.

- `skills`: `List<Skill>`
The initial Skills.

- `tools`: `List<Function<?>>`
The initial tools.

- `maximumRounds`: `Integer`
The maximum rounds.

- `maximumOutputTokens`: `Integer`
The maximum output tokens.

- `toolProvider`: `Function<List<Function<?>>()>?`
The dynamic tool provider.

- `beginToolScope`: `Function<ToolScope()>?`
The tool scope factory.

- `contextProvider`: `Function<String?()>?`
The context provider.

- `mcp`: `List<McpToolProvider>`
The MCP providers.

- `persist`: `List<PersistProvider>`
Conversation log providers, empty by default.


#### `skill`

Public API declaration skill.

```norm
Agent skill(Skill value)
```

Parameters:

- `value`: `Skill`
The Skill to add.


Returns: `Agent`

#### `skill`

Public API declaration skill.

```norm
Agent skill(String url)
```

Parameters:

- `url`: `String`
The Skill URL.


Returns: `Agent`

#### `tool`

Public API declaration tool.

```norm
Agent tool(Function<?> value)
```

Parameters:

- `value`: `Function<?>`
The tool function.


Returns: `Agent`

#### `mcp`

Public API declaration mcp.

```norm
Agent mcp(McpToolProvider value)
```

Parameters:

- `value`: `McpToolProvider`
The MCP provider.


Returns: `Agent`

#### `onText`

Public API declaration onText.

```norm
Agent onText(Void callback(String text))
```

Parameters:

- `callback`: `Function<Void(String)>`
The text callback.


Returns: `Agent`

#### `chat`

Runs a multi-round model interaction and dispatches tools.

```norm
Response chat(String input, Function<Void(String)>? onResponseStarted, Function<Void(String)>? onMessageStarted, Function<Void(String)>? onText, Function<Void(Message)>? onMessageCompleted, Function<Void(ToolCall)>? onToolCallReceived, Function<Void(ToolCall)>? onToolStarted, Function<Void(ToolResult)>? onToolCompleted, Function<Void(ToolFailure)>? onToolFailed, Function<Void(Response)>? onResponseCompleted, Function<Void(Exception)>? onFailed, Function<Void(String)>? onRunStarted, Function<Void(Response)>? onRunCompleted, Function<Void(GenerationEvent)>? onEvent, AgentSession? session)
```

Parameters:

- `input`: `String`
The user input.

- `onResponseStarted`: `Function<Void(String)>?`
The response-start callback.

- `onMessageStarted`: `Function<Void(String)>?`
The message-start callback.

- `onText`: `Function<Void(String)>?`
The text callback.

- `onMessageCompleted`: `Function<Void(Message)>?`
The message callback.

- `onToolCallReceived`: `Function<Void(ToolCall)>?`
The tool-call callback.

- `onToolStarted`: `Function<Void(ToolCall)>?`
The tool-start callback.

- `onToolCompleted`: `Function<Void(ToolResult)>?`
The tool-complete callback.

- `onToolFailed`: `Function<Void(ToolFailure)>?`
The tool-failure callback.

- `onResponseCompleted`: `Function<Void(Response)>?`
The response callback.

- `onFailed`: `Function<Void(Exception)>?`
The failure callback.

- `onRunStarted`: `Function<Void(String)>?`
The run-start callback.

- `onRunCompleted`: `Function<Void(Response)>?`
The run-complete callback.

- `onEvent`: `Function<Void(GenerationEvent)>?`
The event callback.

- `session`: `AgentSession?`
The session to use.


Returns: `Response`

## `agent.internal`

Source: `internal/Connection.norm`

### `Connection`

```norm
class Connection
```

#### `Connection`

```norm
Connection(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

#### `close`

```norm
Void close()
```

Returns: `Void`

## `agent.internal`

Source: `internal/Database.norm`

### `Database`

```norm
class Database
```

#### `Database`

```norm
Database(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

#### `getConnection`

```norm
Connection? getConnection(String? arg0, String? arg1)
```

Parameters:

- `arg0`: `String?`
- `arg1`: `String?`

Returns: `Connection?`

#### `setUrl`

```norm
Void setUrl(String? arg0)
```

Parameters:

- `arg0`: `String?`

Returns: `Void`

### `databaseNew`

```norm
Database databaseNew()
```

Returns: `Database`

## `agent.internal`

Source: `internal/Statement.norm`

### `Statement`

```norm
class Statement extends JDBC3PreparedStatement implements Codes
```

#### `Statement`

```norm
Statement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

#### `close`

```norm
Void close()
```

Returns: `Void`

#### `executeUpdate`

```norm
Integer executeUpdate()
```

Returns: `Integer`

#### `setString`

```norm
Void setString(Integer arg0, String? arg1)
```

Parameters:

- `arg0`: `Integer`
- `arg1`: `String?`

Returns: `Void`

### `statementNew`

```norm
Statement statementNew(Connection? arg0, String? arg1)
```

Parameters:

- `arg0`: `Connection?`
- `arg1`: `String?`

Returns: `Statement`

## `agent`

Source: `mcp.norm`

### `McpToolProvider`

Public API declaration McpToolProvider.

```norm
interface McpToolProvider
```

#### `definitions`

Lists the tools exposed by the provider.

```norm
List<ToolDefinition> definitions()
```

Returns: `List<ToolDefinition>`

#### `supports`

Checks whether a tool is supported.

```norm
Boolean supports(String name)
```

Parameters:

- `name`: `String`
The tool name.


Returns: `Boolean`

#### `invoke`

Invokes a remote tool.

```norm
String invoke(ToolCall call)
```

Parameters:

- `call`: `ToolCall`
The tool call.


Returns: `String`

### `McpClient`

Public API declaration McpClient.

```norm
class McpClient implements McpToolProvider
```

#### `McpClient`

Creates an MCP client.

```norm
McpClient(String endpoint, HttpClient client, Duration timeout)
```

Parameters:

- `endpoint`: `String`
The MCP endpoint.

- `client`: `HttpClient`
The HTTP client.

- `timeout`: `Duration`
The request timeout.


#### `definitions`

Public API declaration definitions.

```norm
List<ToolDefinition> definitions()
```

Returns: `List<ToolDefinition>`

#### `supports`

Public API declaration supports.

```norm
Boolean supports(String name)
```

Parameters:

- `name`: `String`
The tool name.


Returns: `Boolean`

#### `invoke`

Public API declaration invoke.

```norm
String invoke(ToolCall call)
```

Parameters:

- `call`: `ToolCall`
The tool call.


Returns: `String`

## `agent.org.sqlite.core`

Source: `org/sqlite/core/Codes.norm`

### `Codes`

```norm
interface Codes
```

## `agent.org.sqlite.core`

Source: `org/sqlite/core/CorePreparedStatement.norm`

### `CorePreparedStatement`

```norm
class CorePreparedStatement extends JDBC4Statement implements Codes
```

#### `CorePreparedStatement`

```norm
CorePreparedStatement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

## `agent.org.sqlite.core`

Source: `org/sqlite/core/CoreStatement.norm`

### `CoreStatement`

```norm
class CoreStatement implements Codes
```

#### `CoreStatement`

```norm
CoreStatement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

## `agent.org.sqlite.jdbc3`

Source: `org/sqlite/jdbc3/JDBC3PreparedStatement.norm`

### `JDBC3PreparedStatement`

```norm
class JDBC3PreparedStatement extends CorePreparedStatement implements Codes
```

#### `JDBC3PreparedStatement`

```norm
JDBC3PreparedStatement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

## `agent.org.sqlite.jdbc3`

Source: `org/sqlite/jdbc3/JDBC3Statement.norm`

### `JDBC3Statement`

```norm
class JDBC3Statement extends CoreStatement implements Codes
```

#### `JDBC3Statement`

```norm
JDBC3Statement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

## `agent.org.sqlite.jdbc4`

Source: `org/sqlite/jdbc4/JDBC4Statement.norm`

### `JDBC4Statement`

```norm
class JDBC4Statement extends JDBC3Statement implements Codes
```

#### `JDBC4Statement`

```norm
JDBC4Statement(__JarBindingToken token)
```

Parameters:

- `token`: `__JarBindingToken`

## `agent`

Source: `persist.norm`

### `PersistProvider`

Receives ordered events for a conversation. The session identifier is generated by the library.

```norm
interface PersistProvider
```

#### `append`

Appends one event.

```norm
Void append(String sessionId, JsonValue event)
```

Parameters:

- `sessionId`: `String`
The conversation identifier.

- `event`: `JsonValue`
The event object.


Returns: `Void`

### `JsonPersist`

Appends UTF-8 JSON Lines to a generated file per session.

```norm
class JsonPersist implements PersistProvider
```

#### `JsonPersist`

Creates a JSON Lines provider.

```norm
JsonPersist(String directory)
```

Parameters:

- `directory`: `String`
Output directory, default logs.


#### `append`

Appends and flushes one JSON event.

```norm
Void append(String sessionId, JsonValue event)
```

Parameters:

- `sessionId`: `String`
The conversation identifier.

- `event`: `JsonValue`
The event object.


Returns: `Void`

### `SqlitePersist`

Records ordered events in a generated SQLite database per conversation.

```norm
class SqlitePersist implements PersistProvider
```

#### `SqlitePersist`

Creates a SQLite provider.

```norm
SqlitePersist(String directory)
```

Parameters:

- `directory`: `String`
Output directory, default logs.


#### `append`

Commits one event in SQLite.

```norm
Void append(String sessionId, JsonValue event)
```

Parameters:

- `sessionId`: `String`
The conversation identifier.

- `event`: `JsonValue`
The event object.


Returns: `Void`

## `agent`

Source: `session.norm`

### `SessionStore`

Public API declaration SessionStore.

```norm
interface SessionStore
```

#### `load`

Loads the JSON session state.

```norm
JsonValue load()
```

Returns: `JsonValue`

#### `save`

Stores the JSON session state.

```norm
Void save(JsonValue value)
```

Parameters:

- `value`: `JsonValue`
The JSON state.


Returns: `Void`

### `JsonSessionStore`

Public API declaration JsonSessionStore.

```norm
class JsonSessionStore implements SessionStore
```

#### `JsonSessionStore`

Creates a JSON session store.

```norm
JsonSessionStore(String initialState)
```

Parameters:

- `initialState`: `String`
The initial JSON state.


#### `load`

Public API declaration load.

```norm
JsonValue load()
```

Returns: `JsonValue`

#### `save`

Public API declaration save.

```norm
Void save(JsonValue value)
```

Parameters:

- `value`: `JsonValue`
The JSON state.


Returns: `Void`

## `agent`

Source: `skill.norm`

### `Skill`

Public API declaration Skill.

```norm
class Skill
```

#### `name`

Public API declaration name.

```norm
String name
```

Type: `String`

#### `url`

Public API declaration url.

```norm
String url
```

Type: `String`

#### `Skill`

Creates a Skill from a remote URL.

```norm
Skill(String url)
```

Parameters:

- `url`: `String`
The Skill URL.


#### `Skill`

Creates a named Skill from a remote URL.

```norm
Skill(String name, String url)
```

Parameters:

- `name`: `String`
The Skill name.

- `url`: `String`
The Skill URL.


### `SkillLoader`

Loads Skills from remote URLs.

```norm
class SkillLoader
```

#### `fetch`

Fetches a Skill document from its URL.

```norm
String fetch(Skill skill, HttpClient client, Duration timeout)
```

Parameters:

- `skill`: `Skill`
The Skill to load.

- `client`: `HttpClient`
The HTTP client.

- `timeout`: `Duration`
The request timeout.


Returns: `String`

