Convert messages into fun encodings

# ,hash
Various hashing commands<br/>
 - Usage: `,hash`
## ,hash md5
MD5 Hash some Text<br/>
 - Usage: `,hash md5 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,hash sha1
SHA1 Hash some Text<br/>
 - Usage: `,hash sha1 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,hash sha512
SHA512 Hash some Text<br/>
 - Usage: `,hash sha512 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,hash sha256
SHA256 Hash some Text<br/>
 - Usage: `,hash sha256 <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,encode
Encode a string.<br/>
 - Usage: `,encode`
## ,encode b32
Encode text into base 32<br/>
 - Usage: `,encode b32 <message>`
 - Aliases: `base32`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode hex
Encode text into hexadecimal<br/>
 - Usage: `,encode hex <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode chr
Encode message into character numbers<br/>
 - Usage: `,encode chr <message>`
 - Aliases: `character`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode b16
Encode text into base 16<br/>
 - Usage: `,encode b16 <message>`
 - Aliases: `base16`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode binary
Encode text into binary sequences of 8<br/>
 - Usage: `,encode binary <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode braille
Encode text into braille unicode characters<br/>
 - Usage: `,encode braille <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode dna
Encodes a string into DNA 4 byte ACGT format<br/>
 - Usage: `,encode dna <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode b64
Encode text into base 64<br/>
 - Usage: `,encode b64 <message>`
 - Aliases: `base64`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,encode rot
Encode a caeser cipher message with specified key<br/>
 - Usage: `,encode rot <rot_key> <message>`
 - Aliases: `caeser`
Extended Arg Info
> ### rot_key: Optional[int]
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# ,decode
Decode a string.<br/>
 - Usage: `,decode`
## ,decode b16
Decode base16 text<br/>
 - Usage: `,decode b16 <message>`
 - Aliases: `base16`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode chr
Decode character numbers to a message<br/>
 - Usage: `,decode chr <message>`
 - Aliases: `character`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode dna
Decodes a string of DNA in 4 byte ACGT format.<br/>
 - Usage: `,decode dna <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode rot
Decode a caeser cipher message with specified key<br/>
 - Usage: `,decode rot <rot_key> <message>`
 - Aliases: `caeser`
Extended Arg Info
> ### rot_key: Optional[int]
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode hex
Decode a hexadecimal sequence to text<br/>
 - Usage: `,decode hex <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode binary
Decode binary sequences of 8<br/>
 - Usage: `,decode binary <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode b32
Decode base32 text<br/>
 - Usage: `,decode b32 <message>`
 - Aliases: `base32`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode braille
Decide braille unicode characters to ascii<br/>
 - Usage: `,decode braille <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## ,decode b64
Decode base 64 text<br/>
 - Usage: `,decode b64 <message>`
 - Aliases: `base64`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
