
from funcx_endpoint.endpoint.utils.config import Config
from parsl.providers import GridEngineProvider
from parsl.addresses import address_by_route

config = Config(provider=GridEngineProvider(walltime='10000:00:00',
                                            nodes_per_block=1,
                                            init_blocks=1,
                                            max_blocks=4,
                                            scheduler_options="#$ -pe smp 1"
                                            )
)

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "blt_small",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    # Adam UUID
    "visible_to": ["urn:globus:auth:identity:57bc2f29-7689-4268-9f09-31e0ad14adab"]
}
