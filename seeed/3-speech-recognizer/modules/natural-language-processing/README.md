# Natural Language Processing - spacY
[spaCy](https://spacy.io) is a natural language processing library used to extract entities, parts of speech (noun/verb/etc.), dependency parsing, and other language understanding tasks.  This builds a container that takes text (sentences) as input and extracts meaning.

Build the container for Python 2.7:

```
%> docker build --rm -t natural-language-processing:1.0-arm32v7 -f Dockerfile.arm32v7 .
```

Run the container:

```
// Run the container on arm32v7 (e.g. Raspberry Pi 3):
%> docker run --rm -p 8080:8080 natural-language-processing:1.0-arm32v7
```

Query the container:

```
%> curl -X POST http://localhost:8080/chat -d "Hello"
"How are you!"
