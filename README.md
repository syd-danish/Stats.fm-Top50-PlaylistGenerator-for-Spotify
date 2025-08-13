<!DOCTYPE html>
<html lang="en">
<body>

  <h1>🎵 Stats.fm to Spotify Playlist Generator</h1>

  <p>This Python script scrapes your top tracks from <strong>Stats.fm</strong> and automatically creates a <strong>private Spotify playlist</strong> with those songs.</p>

  <h2>📌 Features</h2>
  <ul>
    <li>Scrapes top songs from your Stats.fm profile</li>
    <li>Searches for those songs on Spotify</li>
    <li>Creates a new private Spotify playlist and adds those songs</li>
    <li>Supports multiple ranges like last 4 weeks, last 6 months, or all-time</li>
  </ul>

  <h2>🛠️ Setup Instructions</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/syd-danish/Stats.fm-Top50-PlaylistGenerator-for-Spotify.git
cd Top50-PlaylistGenerator-for-Spotify </code></pre>

  <h3>2. Install Required Packages</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. Create a Spotify Developer App</h3>
  <ol>
    <li>Go to <a href="https://developer.spotify.com/dashboard" target="_blank">Spotify Developer Dashboard and Login or Sign Up </a></li>
    <li>Create a new app</li>
    <li>Copy your <code>Client ID</code> and <code>Client Secret</code></li>
    <li>Set the redirect URI to: <code>https://example.com</code></li>
  </ol>

  <h3>4. Find Your Stats.fm Username</h3>
  <p>Login to <a href="https://stats.fm/" target="_blank">Stats.fm</a> and go to your profile. Copy your username from the URL: <br><code>https://stats.fm/user/&lt;your_username&gt;</code></p>

  <h3>5. Update Your Script</h3>
  <p>Edit the following variables in <code>main.py</code>:</p>
  <ul>
    <li><code>CLIENT_ID = </code></li>
    <li><code>CLIENT_SECRET = </code></li>
    <li><code>USER_String</code> – your Stats.fm username</li>
    <li><code>CHROME_DRIVER_PATH</code> – path to your local chromedriver</li>
  </ul>

  <h3>6. Run the Script</h3>

  <h2>📂 Output</h2>
  <p>The script will create a playlist on your Spotify account named something like:</p>
  <blockquote><code>Your Top 50 Songs - 4 Weeks/6 Months/Lifetime</code></blockquote>

  <h2>💡 Notes</h2>
  <ul>
    <li>Make sure <strong>Brave Browser</strong> is installed if you're using it, or adjust the script to use Chrome or another browser.</li>
    <li>You must be logged into your Stats.fm profile in the browser for the scraper to work correctly.</li>
    <li>This script is intended for personal use only.</li>
  </ul>

  <h2>🔐 Disclaimer</h2>
  <p>Keep your Spotify credentials and token file secure. Do not share them publicly.</p>

  <h2>📄 License</h2>
  <p>This project is licensed under the MIT License.</p>

</body>
</html>

