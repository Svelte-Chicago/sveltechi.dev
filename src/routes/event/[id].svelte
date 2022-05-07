<script>
    import { page } from '$app/stores';
    import events from '../../data/events.json';

    const UNIX_TIMESTAMP_MULTIPLIER = 1000;

    const id = $page.params.id;

    const getEvent = () => {
        return events.filter(ev => ev.id == id)
    }
    // async function getEvent(id) {

    //     const response =  await fetch(`/api/event/${id}`);
    //     const data = await response.json();
    //     return data;
    // }

    function date_format(timestamp) {
        // TODO: make this prettier
        return new Date(timestamp*UNIX_TIMESTAMP_MULTIPLIER)
    }

    const ev = getEvent()[0]

</script>


<div class="relative top-12 max-w-3xl flex flex-row justify-center pl-4 pr-4">
    <div class="border-primary lg:h-[10rem] lg:w-[10rem] h-28 w-28 bg-white border-8 rounded-full p-4 aspect-square">
        <img src="/svelte_chicago_125x125.png" alt="Svelte Society Chicago Logo" />
    </div>
    <div class="pl-8 flex flex-col align-middle">
        <div class="text-xl">Event: {ev.Title}</div>
        <div><span class="font-bold">When:</span> {date_format(ev.Date)} </div>
        <div><span class="font-bold">Where: </span>{ev.Location}</div>
        <div><span class="font-bold">What: </span>{ev.Description}</div>
    </div>
</div>
<div class="pt-[8rem] text-2xl">
    <!-- Signup form will go below -->
    We're just getting started! Sign-ups will be open soon
</div>

