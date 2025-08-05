<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spotify Stats.fm Playlist Generator</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 2em; line-height: 1.6;">
    <h1>🎧 Spotify Stats.fm Playlist Generator</h1>
    <p>This Python script scrapes your top 50 tracks from <strong>Stats.fm</strong> and creates a new private playlist in your <strong>Spotify</strong> account with those songs.</p>

    <h2>🚀 Features</h2>
    <ul>
        <li>Scrapes top 50 tracks from your Stats.fm public profile</li>
        <li>Searches for tracks on Spotify using the Spotipy API</li>
        <li>Automatically creates a private playlist with those songs</li>
    </ul>

    <h2>📦 Requirements</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>Google Chrome or Brave Browser</li>
        <li>Installed ChromeDriver or BraveDriver</li>
        <li>Spotify Developer account</li>
        <li>Stats.fm account</li>
    </ul>

    <h2>🔑 Setup Instructions</h2>
    <ol>
        <li>
            <strong>Spotify Developer Setup:</strong><br>
            <ol type="a">
                <li>Go to <a href="https://developer.spotify.com/dashboard" target="_blank">Spotify Developer Dashboard</a></li>
                <li>Log in and create a new app</li>
                <li>Copy your <strong>Client ID</strong> and <strong>Client Secret</strong></li>
                <li>Set a redirect URI (e.g., <code>https://example.com</code>) in the app settings</li>
            </ol>
        </li>
        <li>
            <strong>Stats.fm Setup:</strong><br>
            <ol type="a">
                <li>Go to <a href="https://stats.fm" target="_blank">Stats.fm</a></li>
                <li>Log in and go to your profile</li>
                <li>Copy your username from the URL (e.g., <code>https://stats.fm/user/&lt;username&gt;</code>)</li>
            </ol>
        </li>
        <li>
            <strong>Install dependencies:</strong><br>
            Run the following in your terminal:
            <pre><code>pip install selenium spotipy beautifulsoup4</code></pre>
        </li>
        <li>
            <strong>Download ChromeDriver:</strong><br>
            Download the version matching your browser from <a href="https://chromedriver.chromium.org/downloads" target="_blank">here</a> and set the path in the script as <code>CHROME_DRIVER_PATH</code>.
        </li>
        <li>
            <strong>Run the script:</strong><br>
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

    <h2>📝 Notes</h2>
    <ul>
        <li>Make sure your Stats.fm profile is public.</li>
        <li>The script supports different time ranges (weeks, months, lifetime). Change the index if needed.</li>
        <li>Some songs may not be found in Spotify and will be skipped.</li>
    </ul>

    <h2>📁 File Structure</h2>
    <ul>
        <li><code>main.py</code> – Core script</li>
        <li><code>requirements.txt</code> – Required Python packages</li>
        <li><code>chromedriver</code> – ChromeDriver executable</li>
    </ul>

    <h2>🙌 Credits</h2>
    <p>Made with ❤️ using Python, Selenium, BeautifulSoup, and Spotipy</p>
</body>
</html>
