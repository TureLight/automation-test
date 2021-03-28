from typing import List
from pydantic import BaseModel


# Shared properties
class DataBody(BaseModel):
    case_num: int
    task_case_num: int
    run_time: str
    task_progress: int


class PieDataBody(BaseModel):
    name: str
    value: int


class PanelGroupData(BaseModel):
    code: int
    message: str
    data: DataBody


class PieChartData(PanelGroupData):
    data: List[PieDataBody]


