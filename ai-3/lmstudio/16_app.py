import lmstudio as lms

downloaded = lms.list_download_models()
llm_only = lms.list_downloaded_models(llm_only=True)
embbding_only = lms.list_downloaded_models(embedding_only=True)

for model in downloaded:
    print(model)
print('-' * 50)

for model in llm_only:
    print(model)
print('-' * 50)

for model in embbding_only:
    print(model)
print('-' * 50)
