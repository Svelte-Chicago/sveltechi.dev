<script>
    import Icon from 'svelte-awesome';
    import { twitter, github } from 'svelte-awesome/icons';

    const socials = [{
        icon: twitter,
        url: 'https://twitter.com/SvelteChicago'
    },{
        icon: github,
        url: 'https://github.com/svelte-chicago/'
    }]
</script>


<div class='w-full relative max-w-4xl h-full min-h-screen text-center border-primary border-l-2 border-r-2'>
    <!-- Chicago Flag -->
    <img src="/chicago_flag.svg" class='w-full' alt="Flag of the City of Chicago"/>

    <!-- Logo and images -->
    <div class="flex items-center justify-start gap-x-4 ml-8 lg:ml-24 -mt-4 lg:-mt-48">
        <div class="border-primary lg:h-[10rem] lg:w-[10rem] h-28 w-28 bg-white border-8 rounded-full p-4 aspect-square">
            <img src="/svelte_chicago_125x125.png" alt="Svelte Society Chicago Logo" />
        </div>
        {#each socials as {url, icon} (url)}
            <div class="text-primary lg:w-36 h-20 w-20 rounded-full">
                <a href="{url}" target="_new"><Icon data={icon} scale="4" class="bg-white w-full h-full border-2 p-2 lg:p-0 border-primary rounded-full aspect-square" /></a>
            </div>
        {/each}
    </div>

    <!-- Body Text -->
    <div class='text-left px-8 md:px-32 mt-12'>
        <div class="text-4xl mb-3">
            Svelte Society: Chicago
        </div>
        <div class="text-xl pb-8">
            We're just getting started and aim to be <a href="https://sveltesociety.dev/about/" class="text-primary underline">an inclusive group for all</a> to share their svelte stories - find us on Twitter and GitHub or
            join us at an <a href="/events" class="text-primary underline">event</a>
        </div>
    </div>
</div>

