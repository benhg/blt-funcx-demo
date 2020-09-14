from funcx.config import Config
from parsl.providers import GridEngineProvider
from parsl.addresses import address_by_route

config = Config(provider=GridEngineProvider(walltime='10000:00:00',
                                            nodes_per_block=1,
                                            init_blocks=1,
                                            max_blocks=4,
                                            scheduler_options="#$ -q gpu.q"),
                 cores_per_worker=1,
                 )

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "blt_gpu",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    "visible_to": []
}
