import pytest


@pytest.fixture
def sample_html():
    return """
    <html>
    <p><strong>Bold text.</strong></span></p>
    <h1>Header 1</h1>
    <h2>Header 2</h2>
    <h3>Header 3</h3>
    
    <p>List:</p>
    <ul>
    <li><strong>Bold list</li>
    <li>Regular list</li>
    </ul>
    
    <p><img src="https://sample/img.jpg" alt="text"/></p>
    <p><a href="/">link></a></p>
    
    </html>
    """