from aur.report import return_full_report

report = return_full_report(
    "examples/weird.csv",
    30
)

print(report)