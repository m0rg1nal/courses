import csv

with open('names.csv', 'r') as csv_general:
    csv_reader = csv.DictReader(csv_general)

    with open('emails.csv', 'w', newline='') as csv_emails:
        fieldnames = ['email']
        csv_writer = csv.DictWriter(csv_emails, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['last_name'], line['first_name']
            csv_writer.writerow(line)