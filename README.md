> [!NOTE]
> See `main.py` to view script used to "scrape" the summaries (only 23k because of their rate-limiting).
> If you want to run `main.py`, make sure to install `pymediawiki` using `pip install pymediawiki.`
> See APPENDIX A for licensing background.  
> See APPENDIX B for restrictions on commercial use (also applies to models trained on this data).
---
**Summary**:
- 23,000 Wikipedia articles with title-summary pairs
- JSON format with { "title": "summary", ... 22,999 times }
- Articles generally CC BY-SA 4.0 licensed, and the license allows commercial use assuming:
  - Credits are given to authors
  - Provide a link to the same license
  - Indicate how the data was used or what changes were made
  - If you modify the dataset itself, derivates must be licensed alike
- That's licensing Wikipedia enforces, not me, but these are still to be respected
---
```
APPENDIX A
---
By using this dataset, you comply with following rules outlined by Wikipedia's editors and similar, summarized using Mistral.
---
Wikipedia License

The text content on Wikipedia is primarily licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).
This license allows for free use, modification, and redistribution of the content, provided that the new work is also licensed under the same or a compatible license, proper attribution is given to the original authors, and any modifications are indicated.
Attribution can be fulfilled by including a hyperlink or URL to the original Wikipedia page, a stable online copy, or a list of the authors.

For compatibility reasons, Wikipedia's text is also co-licensed under the GNU Free Documentation License (GFDL), but only for content published before June 15, 2009, or content that is dual-licensed.
However, since June 15, 2009, the CC BY-SA 4.0 license has been the primary license for new text contributions, and the GFDL is now considered a secondary license.
Content imported from external sources after this date may only be licensed under CC BY-SA or a CC BY-SA-compatible license and cannot be reused under the GFDL alone.

It is crucial to verify the specific license for each piece of content, as the page footer, history, or discussion page may indicate if a page is exclusively licensed under CC BY-SA or contains content not compatible with the GFDL.
Additionally, images and other media files on Wikipedia are subject to their own individual licenses, which must be checked on the file's description page, as they may be in the public domain, under different free licenses, or used under "fair use" provisions.

Reusing Wikipedia content requires compliance with the applicable license terms, including proper attribution and licensing of derivative works.
The Wikimedia Foundation does not provide legal advice, and users are responsible for ensuring their reuse complies with both the license and the laws of their jurisdiction.
```

```
APPENDIX B
---
As APPENDIX A, this is summarized using relevant web-queries using Mistral.
---
CC BY-SA 4.0 Commercial Use

Yes, commercial use is permitted under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.
This means you can use, distribute, and adapt the material for commercial purposes, such as selling products or services based on it.
However, you must give appropriate credit to the original creator, provide a link to the license, and indicate if changes were made.
Furthermore, if you remix, transform, or build upon the material, you must distribute your new creations under the same CC BY-SA 4.0 license.
This requirement is known as "ShareAlike" and ensures that derivative works remain freely available under the same terms.
It is important to note that while the license allows commercial use, Creative Commons itself discourages the use of its licenses for software, recommending more suitable licenses like the GNU GPL for such works.
```

```
Simple JSON-based dataset which contains exactly 23,000 summaries of many Wikipedia articles, mapped to their title, with Pakistan as a seed and it's linked articles used squentially (deduplicated, of course).
The dataset is fully self-contained in "./data.json" in the root directory.
The structure of "./data.json" is simple and easy you "plug-in-play" using Python's standard JSON library and or simple C/C++ functions for parsing the structure:
---
{
  "title": "summary",
  "title": "summary",
  ... you get it
}
---
Here's an example Python script for loading it into a variable named "data":
---
from json import loads

# Load data into "data"
with open("data.json", 'r') as r:
  data = loads(r.read())

# Keys are titles as mentioned above
titles: list[str] = list(data.keys())

# Summaries are values as mentioned above
summaries: list[str] = list(data.values())
---
```
