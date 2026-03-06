import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("sundar pichai is the CEO of google and lives in california for the last 20 years")
# for token in doc:
#     print(token.text, token.pos_,token.lemma_, token.is_stop) 

# print(nlp.pipe_names)

for ent in doc.ents:
    print(ent.text, ent.label_)