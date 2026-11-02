---
title: "Pythoni meelespea · Eesti"
nav_order: 2
lang: et
description: "Lühike Pythoni meelespea failis script.py kasutatud mõistete kohta."
---

# Pythoni meelespea

[In English]({{ '/' | relative_url }})

Ainult failis `script.py` kasutatud mõisted. Leia vajalik mõiste, võrdle näidet oma koodiga, muuda üht asja ja käivita uuesti. Iga koodiplokk on eraldi näide.

## Muutujad ja andmetüübid

`=` salvestab väärtuse muutujasse. Uus omistamine asendab eelmise väärtuse. Suur- ja väiketähed loevad: `age` ja `Age` on erinevad nimed.

```python
name = "Alice"       # str: tekst ehk sõne (jutumärkides)
age = 25             # int: täisarv
price = 19.99        # float: ujukomaarv (kasuta punkti)
is_active = True     # bool: True või False (jutumärkideta)
```

**Kontrolli:** `"25"` on tekst, `25` on arv. Kommentaar algab märgiga `#`; Python eirab ülejäänud rida.

## Väljund: print ja f-sõned

`print()` kuvab väärtuse. F-sõnes lisab `{name}` teksti sisse muutuja väärtuse.

```python
name = "Ragnar"
print("Täna on hea päev!")
print(f"Tere, {name}!")  # Tere, Ragnar!
```

**Kontrolli:** pane `f` avava jutumärgi ette ja muutuja ümber looksulud `{}`. `print("name")` kuvab sõna, `print(name)` muutuja väärtuse.

## Sisend: küsi ja salvesta

`input()` esitab küsimuse ja tagastab **teksti**, isegi kui sisestad numbreid. Kirjuta vastus ja vajuta Enter.

```python
friendName = input("Mis su nimi on: ")
print(f"Tere, {friendName}!")
```

**Kontrolli:** vastuse kasutamisel kirjuta sama muutuja nimi. Failis `script.py` salvestatakse `friendName`, kuid seda ei kasutata tervituses.

## Arvud: int ja lahutamine

`int()` teisendab täisarvu sisaldava teksti täisarvuks. `-` lahutab arve.

```python
age = input("Kui vana sa oled: ")
birth_year = 2026 - int(age)
print(birth_year)
```

**Kontrolli:** sisesta `12`, mitte `kaksteist` ega `12.5`. Ära lisa küsimuse järele `age = 25`, kui sa ei soovi vastust asendada (failis `script.py` praegu nii juhtub). See hinnang kasutab fikseeritud aastat 2026; tegelik sünniaasta võib olla aasta võrra varasem, kui sünnipäev on veel ees.

## Funktsioonid: defineeri ja kutsu välja

`def` defineerib korduskasutatava tegevuse. **Väljakutse** käivitab selle. **Parameeter** saab väljakutses antud väärtuse.

```python
def print_hi(name):          # name on parameeter
    print(f"Tere, {name}!")

def tell_story():            # parameetrit pole
    print("Täna on hea päev!")

print_hi("Alice")           # anna üks väärtus
tell_story()                # sulud on ikka vajalikud
```

**Kontrolli:** definitsiooni lõpus on `:`. Kasuta funktsiooni sees ühtlast taanet (neli tühikut). Defineeri funktsioon enne väljakutset; need väljakutsed asuvad funktsiooni kehast väljas.

## Return: tagasta tulemus

`return` lõpetab funktsiooni töö ja saadab väärtuse väljakutsujale tagasi. Salvesta või kasuta seda väärtust. `print()` ainult kuvab seda.

```python
def ask_age():
    return input("Kui vana sa oled: ")

def calculate_birthday_year(age):
    return 2026 - int(age)

age = ask_age()
birth_year = calculate_birthday_year(age)
print(birth_year)
```

**Kontrolli:** `return print(...)`, mida kasutab skripti funktsioon `print_age`, kuvab teksti, kuid tagastab `None` (väärtuse puudumine). Aasta tagastamiseks kasuta `return year`, ainult kuvamiseks `print(...)`.

## Tingimused: if, elif, else

`==` võrdleb väärtusi. Python käivitab esimese sobiva haru; `else` käsitleb ülejäänud vastuseid.

```python
answer = input("Kas sulle meeldib programmeerida (jah/ei): ")
if answer == "jah":
    print("Tore, mulle ka!")
elif answer == "ei":
    print("Pole probleemi!")
else:
    print("Sobivad ainult vastused 'jah' ja 'ei'!")
```

**Kontrolli:** `=` omistab, `==` võrdleb. Hoia `if`, `elif` ja `else` samal taandetasemel, lisa iga rea lõppu `:` ning taanda harude sisu. `Jah` ja `jah ` ei võrdu tekstiga `jah`. Algses skriptis sobivad vastused `yes` ja `no`.

## Skripti käivitamine: main-tingimus

Taandega kood käivitub siis, kui käivitad selle faili otse. See ei käivitu, kui teine fail selle impordib. Kirjuta erikujud täpselt nagu näites.

```python
def tell_story():
    print("Täna on hea päev!")

if __name__ == "__main__":
    tell_story()
```

## Kui kood ei tööta

Loe veateate viimast rida; kontrolli viidatud koodirida ja sellele eelnevat rida.

| Sümptom | Mida esmalt kontrollida? |
|---|---|
| `SyntaxError` | Jutumärkide ja sulgude paarid; puuduv `:`; tingimustes `==` |
| `IndentationError` | Ühtlane taane funktsioonides ja harudes; ära sega tühikuid ja tabeldusmärke |
| `NameError` | Õigekiri ja suurtähed; omista muutujale väärtus ja defineeri funktsioon enne kasutamist |
| `TypeError` | Teisenda sisend enne lahutamist arvuks; anna funktsioonile õige arv argumente |
| `ValueError` funktsioonist `int()` | Sisesta täisarv numbritega, näiteks `12` |
| Midagi ei kuvata | Kutsu funktsioon välja; tagastatud väärtuse kuvamiseks kasuta `print()` |
| Vale nimi või vanus | Kontrolli kasutatavat muutujat ja seda, kas hilisem omistamine asendab vastuse |

Salvesta fail, käivita uuesti ja võrdle tulemust oodatuga.
