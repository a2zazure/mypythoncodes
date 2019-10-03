from pathlib import Path
my_file=Path('pb.jpeg')
if my_file.is_file():
    print('ok')