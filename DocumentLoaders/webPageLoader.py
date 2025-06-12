from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDV7GC/ref=sr_1_1_sspa?crid=39HPAGN86SLEC&dib=eyJ2IjoiMSJ9.QXcsb0Z0ESJq9Dtr851ajKIA-PSF51lVy1lk-up6LpuIF0pBvOREeX8FgC1nc-mhKdx9gw5eF_yt5Gkq4KU7FGgfoefho_UqI9Mgued1HCbHWOx-knjY-IKnpovt8ULO9H-FhEOcIeOX2HO_si99UxrbVr7gbVrqrRadDQEVK_sDJ-zjn9pOggtwSLDAPWXPMRlqiINIS-Qqm3QN08BqJKEJ1vHH6UP3EQNOvXYpXdg.5b1foQXUz5UWRUwwsJVXPQN4dbMTk06kutQcnSeGRn8&dib_tag=se&keywords=macbook&qid=1749764903&sprefix=macboo%2Caps%2C328&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

loader = WebBaseLoader(url)

result = loader.load()

print(result[0].page_content)