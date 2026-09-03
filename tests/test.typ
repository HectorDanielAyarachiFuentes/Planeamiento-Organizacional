
#set page(paper: "a4", numbering: "1 / 1")
#show heading.where(level: 1): it => [
  #text(fill: blue)[#it.body]
]

= Test Heading
Hello world!
