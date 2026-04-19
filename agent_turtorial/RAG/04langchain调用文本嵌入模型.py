from langchain_community.embeddings import DashScopeEmbeddings

model = DashScopeEmbeddings()
res_query = model.embed_query("你好")
print(res_query)
res_document = model.embed_documents(["你好","早上好","晚上好"])
print(res_document)