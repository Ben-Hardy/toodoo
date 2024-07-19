# toodoo

A Command-line todo program that blends in organically with UNIX-like terminal workflows

usage:

- initialize list: `toodoo init` 
- list all current incomplete entries:`toodoo list`
- list all high priority entries: `toodoo list hi`
- list all completed entries: `toodoo list completed`
- add an entry: `toodoo add "entry text here"`
- add an entry with a specific priority (options are low, med, hi): `toodoo add hi "entry text here"`
- mark an entry as complete: `toodoo done [entryID]`
- add completed entry back to incomplete list: `toodoo undo [entryID]`
- update/change priority of entry: `toodoo up [new priority] [entryID]`
