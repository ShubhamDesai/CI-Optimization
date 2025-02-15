# test_database_backup.py

from database_backup import perform_database_backup

def test_perform_database_backup():
    result = perform_database_backup()
    assert result == "Database Backup Complete"
