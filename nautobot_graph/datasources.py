from nautobot.apps.datasources import DatasourceContent


def refresh_git_text_files(repository, job_result, delete=False):
    if "nautobot_graph.textfile" in repository.provided_contents:
        job_result.log(message="Refreshed text files")


datasource_contents = [
    (
        "extras.gitrepository",
        DatasourceContent(
            name="text files",
            content_identifier="nautobot_graph.textfile",
            icon="mdi-note-text",
            callback=refresh_git_text_files,
        ),
    ),
]
