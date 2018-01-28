# Python Debugging with PDB

## PDB

### PDB Links
- https://docs.python.org/3/library/pdb.html

### PDB Usage in a File
- import pdb
- pdb.set_trace()

### Advantages
- no IDE required
- can run on server

### Using a PDB Breakpoint

| Code | Function | Description  |
| :-------------: |:-------------:| -----|
| l | list | list 11 surrounding lines of code |
| ll | long list | list lines of code for current function or name |
| w | where      |  show stack trace |
| n | next   |  execute next line |
| s | step   |  step into function |
| a | arguments   |  will reveal all arguments |
| c | continue   |  continue until next break point |
| unt [#] | until   |  continue until specified line number |
| r | return   |  run until function return executes |
| b [#] | breakpoint   | set breakpoint at specified line (i.e. b100) |
| cl [#] | clear   | clear breakpoint at specified line (i.e. b100) |
| p [var] | print | print value of a variable |
| pp [var] | pretty-print | pretty-print value of a variable |
| q | quit  |  quit the debugger |

#### Skip Remaining set_trace Breakpoints Hack
```python
pdb.set_trace = lambda: None
c
```

#### Multiline Statements and Loops
- launch a temporary interactive Python session with all the local variables available
    - will turn pdb into an interactive shell
    - [Ctrl] [D] to return to the regular pdb prompt

```python
!import code; code.interact(local=vars())
```   
