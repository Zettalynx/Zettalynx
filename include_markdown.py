def include_markdown(source_file, target_file, marker_start, marker_end):
    with open(source_file, 'r') as src:
        content = src.read()

    with open(target_file, 'r') as tgt:
        readme = tgt.read()

    # Insert content between markers
    start_index = readme.find(marker_start)
    end_index = readme.find(marker_end)

    if start_index != -1 and end_index != -1:
        updated_readme = readme[:start_index + len(marker_start)] + '\n' + content + '\n' + readme[end_index:]
        with open(target_file, 'w') as tgt:
            tgt.write(updated_readme)
    else:
        print(f"Markers {marker_start} or {marker_end} not found in {target_file}")

if __name__ == "__main__":
    include_markdown('github_stats.md', 'README.md', '<!-- START_STATS -->', '<!-- END_STATS -->')
