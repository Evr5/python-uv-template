from pytest import CaptureFixture

from main import main


def test_main_output(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from uv template!" in captured.out
