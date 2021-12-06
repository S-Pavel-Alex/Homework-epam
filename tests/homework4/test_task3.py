from homework4.task3 import my_precious_logger


def test_stdout_write_positive(capsys):
    my_precious_logger('please work')
    out, err = capsys.readouterr()
    assert out == 'please work\n'
    assert err == ''


def test_stderr_write_positive(capsys):
    my_precious_logger("error it's bad")
    out, err = capsys.readouterr()
    assert out == ''
    assert err == "error it's bad\n"
