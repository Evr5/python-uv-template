import pytest

# This file allows to define global fixtures or configure pytest.
# Even if empty, it helps pytest identify the project's root directory.


@pytest.fixture(autouse=True)
def setup_testing_env():
    """
    Fixture executed automatically before each test.
    Useful for configuring test environment variables or cleaning up resources.
    """
    # Example: Configuring environment variables for tests
    # os.environ["APP_ENV"] = "test"

    yield
    # Cleanup code if needed after tests
