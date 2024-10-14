from automation.graphs.state import PlanExecuteState
from codebase.base import FileChange


class OverallState(PlanExecuteState):
    diff: str
    show_diff_hunk_to_executor: bool
    request_for_changes: bool
    file_changes: dict[str, FileChange]
