pythonCommands=(
  python3
  python
  py
)

for pythonCommand in ${pythonCommands[*]}
do
    $pythonCommand manage.py runserver --settings=wwustc.dev-settings
done