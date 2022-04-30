<script>
    import Icon from 'svelte-awesome';
    import { twitter, github } from 'svelte-awesome/icons';
</script>


<div class='w-full relative max-w-4xl h-screen text-center border-red-600 border-l-2 border-r-2'>
    <img src="/chicago_flag.svg" class='w-full' alt="Flag of the City of Chicago"/>
    <div class="absolute bottom-[15rem] left-6 align-middle ">
        <div class="border-red-600 lg:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] bg-white border-8 rounded-full p-4 align-middle inline-block">
            <img src="/svelte_chicago_125x125.png" alt="Svelte Society Chicago Logo" />
        </div>
        <div class="text-red-600 g:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] pt-6 inline-block rounded-full align-middle pl-6">
            <a href="https://twitter.com/SvelteChicago"><Icon data={twitter} scale="4" class="bg-white w-full h-full border-2 border-red-600 rounded-full" /></a>
        </div>
        <div class="text-red-600 g:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] pt-6 inline-block rounded-full align-middle pl-6 ">
            <a href="https://github.com/svelte-chicago/"><Icon data={github} scale="4" class="bg-white w-full h-full border-2 border-red-600 rounded-full" /></a>
        </div>
    </div>
    <div class='absolute bottom-[8rem] left-[8rem] text-left'>
        <div class="text-4xl">
            Svelte Society: Chicago
        </div>
        <div class="text-xl">
            We're just getting started - find us on twitter and github
        </div>
    </div>
</div>

