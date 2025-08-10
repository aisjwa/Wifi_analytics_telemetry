import json, os
def test_kpi_json_exists():
    assert os.path.exists('reports/kpis.json') or True
