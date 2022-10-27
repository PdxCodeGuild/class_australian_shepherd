let area = document.querySelector('#area')

const data = `struct group_info init_groups = { .usage = ATOMIC_INIT(2) };

struct group_info *groups_alloc(int gidsetsize){

	struct group_info *group_info;

	int nblocks;

	int i;



	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;

	/* Make sure we always allocate at least one indirect block pointer */

	nblocks = nblocks ? : 1;

	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);

	if (!group_info)

		return NULL;

	group_info->ngroups = gidsetsize;

	group_info->nblocks = nblocks;

	atomic_set(&group_info->usage, 1);



	if (gidsetsize <= NGROUPS_SMALL)

		group_info->blocks[0] = group_info->small_block;

	else {

		for (i = 0; i < nblocks; i++) {

			gid_t *b;

			b = (void *)__get_free_page(GFP_USER);

			if (!b)

				goto out_undo_partial_alloc;

			group_info->blocks[i] = b;

		}

	}

	return group_info;


`

let counter = 0

let buildString = ''

document.body.addEventListener('keypress', (event) => {
    // console.log(event)
    // console.log(`You pressed the key: ${event.key}`)

    for (let i = 0; i < counter; i++) {
      buildString += data[i]
    }


    area.innerHTML = buildString
    buildString = ''
    counter += 3
})

// figure out how to do the access denied popup window at the end of the script. it would be cool if it flashed red
