from google.cloud import dns


client = dns.Client(project="project-id")


def create_cname_record(client, zone_name, cname_name, target):
    zone = client.zone(zone_name)
    record_set = zone.resource_record_set(cname_name, "CNAME", ttl=3600, target=target)
    changes = zone.changes()
    changes.add_record_set(record_set)
    changes.create()


create_cname_record(client, "zone-name", "subdomain.company.net.",)
