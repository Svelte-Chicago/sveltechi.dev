<script>
    const UNIX_TIMESTAMP_MULTIPLIER = 1000;

    import Icon from 'svelte-awesome';
    import { calendar } from 'svelte-awesome/icons';

    import events from '../data/events.json';

    const newEventList = (() => {
        const time = Date.now();
        const data = events.filter(ev => ev.Date > (time / UNIX_TIMESTAMP_MULTIPLIER));
        return data;
    })

    const oldEventList = (() => {
        const time = Date.now();
        const data = events.filter(ev => ev.Date < (time / UNIX_TIMESTAMP_MULTIPLIER));
        return data;
    })

    function date_format(timestamp) {
        // TODO: make this prettier
        return new Date(timestamp*UNIX_TIMESTAMP_MULTIPLIER)
    }

    const new_events = newEventList();
    const old_events = oldEventList();

</script>

<div class="relative top-[3rem] max-w-screen hidden md:block">
    <div class="text-center font-bold text-2xl">Upcoming Events</div>
    <table>
        <thead class="font-bold">
            <td>What?</td><td>Date & Time</td><td>Location</td><td>Description</td><td>Join Us</td>
        </thead>

        {#if new_events.length > 0}
            {#each new_events as ev}
                <tr class="eventrow">
                <td>{ev.Title}</td>
                <td>{date_format(ev.Date)}</td>
                <td>{ev.Location}</td>
                <td>{ev.Description}</td>
                <td class="text-center"><a href="/event/{ev.id}" class="text-primary"><Icon data={calendar} /> Sign Up</a></td>
                </tr>
            {/each}
        {:else}
            <tr><td colspan="5" class="text-center">No upcoming events currently scheduled</td></tr>
        {/if}

    <tr><td colspan="5">&nbsp;</td></tr>
    <tr><td colspan="5">&nbsp;</td></tr>
        <thead class="font-bold">
            <tr>
                <td colspan="5" class="text-center font-bold text-2xl">Past Events</td>
            </tr>
            <td>What?</td><td>Date & Time</td><td>Location</td><td>Description</td><td></td>
        </thead>

        {#if old_events.length > 0}
            {#each old_events as ev}
                <tr class="eventrow">
                    <td>{ev.Title}</td>
                    <td>{date_format(ev.Date)}</td>
                    <td>{ev.Location}</td>
                    <td>{ev.Description}</td>
                <td></td>
                </tr>
            {/each}
        {:else}
                <tr><td colspan="5" class="text-center">No past events yet</td></tr>
        {/if}
    </table>
</div>

<div class="md:hidden w-full relative max-w-4xl h-full min-h-screen pl-4 pr-4">
    <div class="text-center font-bold text-2xl pt-[2.5rem]">Upcoming Events</div>
    {#if new_events.length > 0}
        {#each new_events as ev}
            <div class="eventrow pt-4">
                <p><span class="font-bold">What:</span>{ev.Title}</p>
                <p><span class="font-bold">When:</span>{date_format(ev.Date)}</p>
                <p><span class="font-bold">Where:</span>{ev.Location}</p>
                <p><span class="font-bold">About:</span>{ev.Description}</p>
                <p><a href="/event/{ev.id}" class="text-primary"><Icon data={calendar} /> Sign Up</a></p>
            </div>
        {/each}
    {:else}
            <span class="text-center">No past events yet</span>
    {/if}
    <div class="text-center font-bold text-2xl top-[1.5rem]">Past Events</div>
    {#if old_events.length > 0}
        {#each old_events as ev}
            <div class="eventrow">
                <p><span class="font-bold">What:</span>{ev.Title}</p>
                <p><span class="font-bold">When:</span>{date_format(ev.Date)}</p>
                <p><span class="font-bold">Where:</span>{ev.Location}</p>
                <p><span class="font-bold">About:</span>{ev.Description}</p>
            </div>
        {/each}
    {:else}
            <span class="text-center">No past events yet</span>
    {/if}
</div>

<style>
    td {
        padding: 0 1rem;
    }

    tr.eventrow:nth-child(odd) {
        background-color:#b3ddf2;
    }
</style>