from datetime import datetime, timezone
def to_iso(ts): return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()