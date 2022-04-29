<script>
    import Icon from 'svelte-awesome';
    import { twitter, github } from 'svelte-awesome/icons';
</script>


<div class='w-full relative'>
    <img src="/chicago_flag.svg" class='w-full' alt="Flag of the City of Chicago"/>
    <div class="absolute bottom-6 left-6 align-middle ">
        <div class="border-red-600 lg:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] bg-white border-8 rounded-full p-4 align-middle inline-block">
            <img src="/svelte_chicago_125x125.png" alt="Svelte Society Chicago Logo" />
        </div>
        <div class="text-red-600 g:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] inline-block pl-10 pt-10 align-middle">
            <a href="https://twitter.com/SvelteChicago"><Icon data={twitter} scale="4" /></a>
        </div>
        <div class="text-red-600 g:h-[10rem] lg:w-[10rem] sm:h-[7rem] sm:w-[7rem] inline-block pt-10 align-middle">
            <a href="https://github.com/svelte-chicago/"><Icon data={github} scale="4" /></a>
        </div>
    </div>
</div>
<div class='w-full relative'>
    <div class="text-4xl absolute left-[12rem]">
        Svelte Society: Chicago
    </div>
    <div class="text-xl absolute top-12 left-[12rem]">
        We're just getting started - find us on twitter and github
    </div>

</div>
