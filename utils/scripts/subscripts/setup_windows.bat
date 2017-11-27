@echo off

set pythonCommand=python3
WHERE python3 >nul 2>null
IF %ERRORLEVEL% EQU 0 (
	goto proceed
)

set pythonCommand=python
WHERE python >nul 2>null
IF %ERRORLEVEL% EQU 0 (
	goto proceed
)

set pythonCommand=py
WHERE py >nul 2>null
IF %ERRORLEVEL% EQU 0 (
	goto proceed
)

goto :EOF

:proceed
%pythonCommand% ../../../manage.py makemigrations --settings=wwustc.%1
%pythonCommand% ../../../manage.py migrate --settings=wwustc.%1
%pythonCommand% ../../../manage.py migrate --run-syncdb --settings=wwustc.%1
%pythonCommand% ../../../manage.py collectstatic --noinput --settings=wwustc.%1
