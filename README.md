# Tietokantasovelluksen harjoitustyö: musafoorumi

### Sovelluksen käyttö ja testaaminen:

Sovelluksen päätoiminnallisuus on musiikkijulkaisuista keskustelu tai vapaamuotoisten arvioiden jättäminen. Tietokannassa oleviin julkaisuihin pääsee käsiksi joko suoraan etusivulta tai artistien kautta (aristisivu näyttää kyseisen artistin tietokannassa sijaitsevat julkaisut). Myös hakukenttää voi käyttää artistin tai julkaisun etsimiseen.

Julkaisun sivulla näkee artistin, raidat ja henkilöstön. Jokaisella henkilöstöläisellä on lisäksi oma sivu, jolta näkee, mille julkaisuille tämä on osallistunut. Viestien ja arvosanojen jättäminen on mahdollista ainoastaan julkaisusivulle ja ainoastaan kirjautuneena.

### Sovelluksen koodi

Kaikki polut on toteutettu routes.py-tiedostoon. Kirjautumiseen ja rekisteröitymiseen liittyvä koodi on users.py-tiedostossa. Release-sivujen arvosanoihin ja kommentteihin liittyvä koodi on reviews.py-tiedostossa. Kirjautumista ja rekisteröitymistä lukuun ottamatta joka sivun html-pohja rakentuu layout.html-tiedoston jatkeena. 

SQL-tiedostoja on kaksi: toisessa on pohjat taulukoille, ja toisessa puolestaan julkaisujen tietokanta. Toistaiseksi uuden julkaisun lisääminen tietokantaan on tehtävä manuaalisesti. Schema.sql-tiedosto nollaa julkaisutietokannan aina aktivoidessa. Tämän ansiosta kirjoitusvirheiden korjaukset sekä julkaisujen lisäykset tai poistot päivittyvät automaattisesti.

### Toiminnallisuus:

Kaikille avoimet toiminnot:
- sivuston selaaminen
- hakutoiminto
- kommenttien lukeminen
- käyttäjätilin luominen ja sisäänkirjautuminen

Käyttäjille tarkoitetut toiminnot:
- arvosanan antaminen julkaisulle
- kommenttien kirjoittaminen

Sivusto antaa virheilmoituksen seuraavista tapahtumista:
- Rekisteröityminen:
  - Käyttäjä luo tilin ilman nimeä
  - Käyttäjä luo tilin, jonka nimi on yli 20 merkkiä pitkä
  - Käyttäjä luo tilin, jonka nimi on jo käytössä
  - Käyttäjä ei vahvista salasanaa oikein
  - Käyttäjän antama salasana on liian lyhyt (alle 8 merkkiä)
- Kirjautuminen:
  - Käyttäjä kirjoittaa käyttäjänimen, jota ei ole tietokannassa
  - Käyttäjän antama nimi ja salasana eivät täsmää
- (Lisäksi tyhjät arviot ja kommentit eivät rekisteröidy, mutta tästä ei tule ilmotusta.)


[musafoorumi-tsoha.herokuapp.com](http://musafoorumi-tsoha.herokuapp.com/)
