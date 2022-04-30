<script>
    import { firebaseConfig } from "$lib/firebase";
    import { initializeApp } from "firebase/app";
    import { getFirestore, collection, getDocs } from "firebase/firestore";

    const fb = initializeApp(firebaseConfig);
    const db = getFirestore(fb);

    async function eventList() {
        const eventQuery = await getDocs(collection(db, "Events"));
        return eventQuery.docs;
    }

</script>

<div>
    <table>
        <thead class="font-bold">
            <td>What?</td><td>Date & Time</td><td>Location</td><td>Description</td>
        </thead>

        {#await eventList()}
            <tr>
                <td colspn="4">Getting upcoming events...</td>
            </tr>

        {:then evs}
            {#each evs as ev}
                <tr>
                <td>{ev.data().Title}</td>
                <td>{ev.data().Date.toDate()}</td>
                <td>{ev.data().Location}</td>
                <td>{ev.data().Description}</td>
                </tr>
            {/each}
        {:catch error}
            <tr><td>Could not get events...</td></tr>
        {/await}

    </table>
</div>

<style>
    td {
        padding: 0 1rem;
    }
</style>