from main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from uv template!" in captured.out
