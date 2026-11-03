import logging
 
logging.basicConfig(level=logging.ERROR)
 
def announce():
    print("starting1")
    print("starting2")
    print("starting3")
    logging.error("Request failed")
def test_console_output(capsys):
    announce()
    captured = capsys.readouterr()
    print("Captured:", captured)
    print(f"\n====================\nCaptured output:\n{captured.out}")
    assert "starting" in captured.out
 
def test_log_message(caplog):
    announce()
    print("Caplog:", caplog)
    print(f"Captured log: {caplog.text}")
    assert "Request failed" in caplog.text