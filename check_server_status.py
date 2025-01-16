name: Update Server Status
on:
  schedule:
    - cron: '0 * * * *' # This runs the script every hour

jobs:
  update-status:
    runs-on: ubuntu-latest
    steps:
      - name: Check out the repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Run the status update script
        run: |
          python check_server_status.py

      - name: Commit and push changes
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'github-actions@github.com'
          git add "Server Status.md"
          git commit -m "Update server statuses"
          git push origin main
