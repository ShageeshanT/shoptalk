from shoptalk.conversation_snippet import conversation_snippet


def test_conversation_snippet():
    assert conversation_snippet("hello\nworld") == "hello world"