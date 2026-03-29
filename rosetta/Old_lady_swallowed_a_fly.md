+++
title = "Old lady swallowed a fly"
+++

# Old lady swallowed a fly

```zc
let animals: string[8] = ["fly", "spider", "bird", "cat","dog", "goat", "cow", "horse"];

let phrases: string[8] = [
    "",
    "That wriggled and jiggled and tickled inside her",
    "How absurd to swallow a bird",
    "Fancy that to swallow a cat",
    "What a hog, to swallow a dog",
    "She just opened her throat and swallowed a goat",
    "I don't know how she swallowed a cow",
    "\n  ...She's dead of course"
];

fn sing() {
    for i in 0..8 {
        println "There was an old lady who swallowed a {animals[i]};";
        if i > 0 { println "{phrases[i]}!"; }
        if i == 7 { return; }
        println "";
        if i > 0 {
            for j in i..=1 step -1 {
                print "  She swallowed the {animals[j]} to catch the {animals[j - 1]}";
                if j < 3  { 
                    println ";";
                } else {
                    println ":";
                }
                if j == 2 { println "  {phrases[1]}!"; }
            }
        }
        println "  I don't know why she swallowed a fly - Perhaps she'll die!\n";
    }
}

fn main() {
    sing();
}
```

**Output:**

```
There was an old lady who swallowed a fly;

  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and jiggled and tickled inside her!

  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird!

  She swallowed the bird to catch the spider;
  That wriggled and jiggled and tickled inside her!
  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!

  She swallowed the cat to catch the bird:
  She swallowed the bird to catch the spider;
  That wriggled and jiggled and tickled inside her!
  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!

  She swallowed the dog to catch the cat:
  She swallowed the cat to catch the bird:
  She swallowed the bird to catch the spider;
  That wriggled and jiggled and tickled inside her!
  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a goat;
She just opened her throat and swallowed a goat!

  She swallowed the goat to catch the dog:
  She swallowed the dog to catch the cat:
  She swallowed the cat to catch the bird:
  She swallowed the bird to catch the spider;
  That wriggled and jiggled and tickled inside her!
  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!

  She swallowed the cow to catch the goat:
  She swallowed the goat to catch the dog:
  She swallowed the dog to catch the cat:
  She swallowed the cat to catch the bird:
  She swallowed the bird to catch the spider;
  That wriggled and jiggled and tickled inside her!
  She swallowed the spider to catch the fly;
  I don't know why she swallowed a fly - Perhaps she'll die!

There was an old lady who swallowed a horse;

  ...She's dead of course!
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Old lady swallowed a fly**](https://rosettacode.org/wiki/Old_lady_swallowed_a_fly) in Zen C.

*This article uses material from the Rosetta Code article **Old lady swallowed a fly**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Old_lady_swallowed_a_fly?action=history).*
