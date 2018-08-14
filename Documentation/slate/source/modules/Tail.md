# Contribute to Documentation

## Modules
All the modules are documented in separate markdown files in the modules directory.

### Module Structure

The function module is written in markdown.<br>
It consists of a brief pseudo code and the fortran as well as the python code for that module

<aside class="notice">
All modules must end with a newline character.
</aside>

## Tangling

`tangle.sh` is a bash script that builds a final index.html file which is then reflected in the documentation

<aside class="notice">
Remember — The sequence of files in `tangle.sh` matters
</aside>

```bash
rm ../index.html.md
cat Degrad.md > ../index.html.md
cat Mixer.md >> ../index.html.md
cat Setup.md >> ../index.html.md
cat Density.md >> ../index.html.md
cat Tail.md >> ../index.html.md
```

<aside class="warning">The directory structure is to be preserved for the framework to work properly. </aside>

<aside class="success">Build documentation using <code>sh tangle.sh</code></aside>



