# Search API

An API that search something for you

## Search 

To search something do a get to: 
<code>
https://search-api-flask.herokuapp.com/search?q={what_you_want_to_search}&lang={output_language}
</code>

Request example:
<pre>
<code>
https://search-api-flask.herokuapp.com/search?q=Naruto&lang=pt
</code>
</pre>

Response example:
<pre>
<code>
{
  "content": "Naruto é uma série de mangá escrita e ilustrada por Masashi Kishimoto, que conta a história de Naruto Uzumaki, um jovem ninja que constantemente procura por reconhecimento e sonha em se tornar Hokage, o ninja líder de sua vila. ",
  "field": "Série de mangá",
  "image": "https://img1.ak.crunchyroll.com/i/spire4/5568ffb263f6bcba85a639980b80dd9a1612993223_full.jpg",
  "link": "https://pt.wikipedia.org/wiki/Naruto&sa=U&ved=2ahUKEwiAor_Om-36AhWMMVkFHUngCSwQmhN6BAgNEA4&usg=AOvVaw2Fc-ax1KCQTFvXmb2-drrg",
  "title": "Naruto"
}
</code>
</pre>

The search answer comes from a google search.
<img src="./github/1.png" width="50%" float="center"></img>
