# tsoha
Tietokantasovelluksen harjoitustyö

VÄLIPALAUTUS HUOM. Lukemattomien teknisten hankaluuksien vuoksi tätä ei ole vielä Herokussa. Reposotorioon on ladattu ainoastaan se määrä tiedostoja, jotka toimivat jollakin tasolla, mutta ohjelman ei oleteta olevan testauskunnossa.

Tarkoituksena on tehdä musanörttien keskustelufoorumi. Sovellukseen on taltioitu musiikkijulkaisuja ja niiden tekijöitä (kuten muusikoita, laulunkirjoittajia, äänittäjiä ja tuottajia). Tekijän kautta pääsee "profiiliin", josta näkee muut työt, joihin tämä on osallistunut. Käyttäjät voivat selata julkaisuja, antaa niille arvioita, jättää niiden alle kommentteja sekä vastata toistensa kommentteihin.

Tarvittavia taulukoita (suluissa hahmotelma sarakkeista):

- Releases (id, name, genre, performer, release_date, publisher)
- Tracks (name, release_id)
- Personnel (id, name, role, release_id)
- Reviews (id, reviewer_id, reviewee_id, score)
- Comments (id, release_id, commenter_id, timestamp, reply_status)
- Users (id, name)
