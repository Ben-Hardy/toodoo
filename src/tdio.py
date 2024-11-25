import tdutils
import tddb


def process_input(args: list):
	if len(args) == 1:
		tdutils.print_help()

	if len(args) == 2:
		if args[1] == '-h' or args[1] == 'help':
			tdutils.print_help()
		elif args[1] == 'init':
			tddb.init_db()
		elif args[1] == 'list':
			tddb.list_incomplete()
	else:
		if args[1] == '-h' or args[1] == 'help':
			tdutils.print_help()
		elif args[1] == 'list' and args[2] in ['-lo', '-mid', '-hi']:
			tddb.list_incomplete_by_priority(args[2])
		elif args[1] == 'list' and args[2] == 'complete':
			tddb.list_complete()
