from app.jobs.update_confluence_vectors import update_confluence_vectors
from app.jobs.update_jira_vectors import update_jira_vectors
def update_knowledge_base():
    print("="*60)
    print("Updating Enterprise Knowledge Base")
    print("="*60)
    print("Updating JIRA...\n")
    update_jira_vectors()
    print("Updating Confluence...\n")
    update_confluence_vectors()
    print("Knowledge Base Updated Successfully")
if __name__ == "__main__":
    update_knowledge_base()