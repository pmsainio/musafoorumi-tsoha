# Tietokantasovelluksen harjoitustyö: musafoorumi

### Sovelluksen käyttö ja testaaminen:

Sovelluksen päätoiminnallisuus on musiikkijulkaisuista keskustelu tai vapaamuotoisten arvioiden jättäminen. Tietokannassa oleviin julkaisuihin pääsee käsiksi joko suoraan etusivulta tai artistien kautta (aristisivu näyttää kyseisen artistin tietokannassa sijaitsevat julkaisut). Myös hakukenttää voi käyttää artistin tai julkaisun etsimiseen.

Julkaisun sivulla näkee artistin, raidat ja henkilöstön. Jokaisella henkilöstöläisellä on lisäksi oma sivu, jolta näkee, mille julkaisuille tämä on osallistunut. Viestien jättäminen on mahdollista ainoastaan julkaisusivulle ja ainoastaan kirjautuneena.

### Sovelluksen koodi

Suurin osa toiminnallisuudesta on toteutettu routes.py-tiedostoon. Templates-kansiossa on sivupohjat etusivulle, kirjautumiselle ja rekisteroitymiselle; artisti-, julkaisu- ja henkilöstösivuille sekä hakutuloksille. SQL-tiedostoja on kaksi: toisessa on pohjat taulukoille, ja toisessa puolestaan julkaisujen tietokanta. Toistaiseksi uuden julkaisujen lisääminen tietokantaan on tehtävä manuaalisesti. Schema.sql-tiedosto nollaa julkaisutietokannan aina aktivoidessa. Tämän ansiosta kirjoitusvirheiden korjaukset sekä julkaisujen lisäykset tai poistot päivittyvät automaattisesti.

### Suunniteltua toiminnallisuutta

Ainoa suunniteltu puuttuva toiminnallisuus on numeroarvion (1--5 tai 1--10) jättämismahdollisuus. Julkaisuille voi näin laskea lisäksi keskiarvon, ja foorumin käyttömahdollisuus levyarvioalustana helpottuu. Tätä varten on jo olemassa taulukko. Lisäksi pitäisi ehkä asettaa foorumille jonkinlainen moderaattori, joka voisi poistaa törkyviestejä.

[musafoorumi-tsoha.herokuapp.com](http://musafoorumi-tsoha.herokuapp.com/)
